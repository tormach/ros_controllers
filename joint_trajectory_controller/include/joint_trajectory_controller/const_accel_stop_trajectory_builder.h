///////////////////////////////////////////////////////////////////////////////
// Copyright (C) 2021, Tormach, Inc.
// Copyright (C) 2013, PAL Robotics S.L.
// Copyright (c) 2008, Willow Garage, Inc.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//   * Redistributions of source code must retain the above copyright notice,
//     this list of conditions and the following disclaimer.
//   * Redistributions in binary form must reproduce the above copyright
//     notice, this list of conditions and the following disclaimer in the
//     documentation and/or other materials provided with the distribution.
//   * Neither the name of PAL Robotics S.L. nor the names of its
//     contributors may be used to endorse or promote products derived from
//     this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.
//////////////////////////////////////////////////////////////////////////////
#ifndef CONST_ACCEL_STOP_TRAJECTORY_BUILDER_H
#define CONST_ACCEL_STOP_TRAJECTORY_BUILDER_H

#include <vector>

#include <joint_trajectory_controller/trajectory_builder.h>
#include <joint_trajectory_controller/tolerances.h>

namespace joint_trajectory_controller
{
/**
 * @brief Builder creating a trajectory stopping the robot.
 */
template <class SegmentImpl>
class ConstAccelStoptrajectoryBuilder : public TrajectoryBuilder<SegmentImpl>
{
private:
  using Segment = JointTrajectorySegment<SegmentImpl>;
  using TrajectoryPerJoint = std::vector<Segment>;
  using Trajectory = std::vector<TrajectoryPerJoint>;

  using RealtimeGoalHandle = realtime_tools::RealtimeServerGoalHandle<
      control_msgs::FollowJointTrajectoryAction>;
  using RealtimeGoalHandlePtr = boost::shared_ptr<RealtimeGoalHandle>;

public:
  /**
   * @param stop_traj_duration Desired time span [seconds] in which the settle
   * position has to be reached.
   * @param hold_state Reference to the state where the stop motion shall start.
   *
   * @note If there is a time delay in the system it is better to calculate the
   * stop trajectory starting from the desired position. Otherwise there would
   * be a jerk in the motion.
   */
  ConstAccelStoptrajectoryBuilder(
      const typename Segment::Time& stop_traj_duration,
      std::vector<double> const& tolerances,
      const typename Segment::State& hold_state);

public:
  /**
   * @brief Creates a trajectory which reaches a final position while respecting
   * the specified acceleration limits.
   *
   * 1) First, based on the current joint velocity, compute the worst-case
   * stopping time required to be within acceleration limits. 2) Compute initial
   * / final conditions for a "quintic" spline path for all joints that reduces
   * to a quadratic (constant acceleration). 3) Build the stop trajectory using
   * the standard spline generator and the computed constraints.
   *
   * @returns true if the building of the stop trajectory succeeds, otherwise
   * false.
   */
  bool buildTrajectory(Trajectory* hold_traj) override;

protected:
  const std::vector<double> max_accelerations_;
  const typename Segment::Time stop_traj_duration_;
  //! @brief Stores a reference to the state where the stop motion shall start.
  const typename Segment::State& hold_state_;

private:  // Pre-allocated memory for real time usage of build function
  typename Segment::State hold_start_state_{ typename Segment::State(1) };
  typename Segment::State hold_end_state_{ typename Segment::State(1) };
};

template <class SegmentImpl>
ConstAccelStoptrajectoryBuilder<SegmentImpl>::ConstAccelStoptrajectoryBuilder(
    const typename Segment::Time& stop_traj_duration,
    std::vector<double> const& tolerances,
    const typename Segment::State& hold_state)
  : max_accelerations_(tolerances)
  , stop_traj_duration_(stop_traj_duration)
  , hold_state_(hold_state)
{
}

template <class SegmentImpl>
bool ConstAccelStoptrajectoryBuilder<SegmentImpl>::buildTrajectory(
    Trajectory* hold_traj)
{
  const unsigned int number_of_joints = hold_state_.position.size();

  if (!TrajectoryBuilder<SegmentImpl>::getStartTime())
  {
    return false;
  }

  if (!TrajectoryBuilder<SegmentImpl>::isTrajectoryValid(hold_traj,
                                                         number_of_joints, 1))
  {
    return false;
  }

  const typename Segment::Time start_time{
    TrajectoryBuilder<SegmentImpl>::getStartTime().value()
  };
  RealtimeGoalHandlePtr goal_handle{
    TrajectoryBuilder<SegmentImpl>::createGoalHandlePtr()
  };

  // 1) compute the worst-case stop duration based on prescribed limits

  double ts = 0;
  for (unsigned int joint_index = 0; joint_index < number_of_joints;
       ++joint_index)
  {
    ts = std::max(ts, std::abs(hold_state_.velocity[joint_index] /
                               max_accelerations_[joint_index]));
  }

  const typename Segment::Time end_time{ start_time + ts };

  for (unsigned int joint_index = 0; joint_index < number_of_joints;
       ++joint_index)
  {
    auto const v0 = hold_state_.velocity[joint_index];
    auto const p0 = hold_state_.position[joint_index];
    const double a = ts > 0 ? -v0 / ts : 0;

    hold_start_state_.position[0] = p0;
    hold_start_state_.velocity[0] = v0;
    hold_start_state_.acceleration[0] = a;

    hold_end_state_.position[0] = p0 + v0 * ts / 2.;
    hold_end_state_.velocity[0] = 0.0;
    hold_end_state_.acceleration[0] = a;

    Segment& segment{ (*hold_traj)[joint_index].front() };
    segment.init(start_time, hold_start_state_, end_time, hold_end_state_);

    segment.setGoalHandle(goal_handle);
  }

  return true;
}

}  // namespace joint_trajectory_controller

#endif  // STOP_TRAJECTORY_BUILDER_H

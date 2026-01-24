class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        def goBack(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(pos, robot, d, lookup):
            # If the position is already cleaned, return
            if pos in lookup:
                return

            # Mark the position as cleaned
            lookup.add(pos)
            robot.clean()

            # Attempt to move in each of the 4 possible directions
            for _ in range(4):
                new_x, new_y = pos[0] + directions[d][0], pos[1] + directions[d][1]

                if robot.move():
                    dfs((new_x, new_y), robot, d, lookup)
                    goBack(robot) #backtracking

                # Rotate the robot to the next direction
                robot.turnRight()
                d = (d + 1) % 4

        # Start DFS from the initial position (0, 0) with the initial direction facing "up" (index 0)
        dfs((0, 0), robot, 0, set())

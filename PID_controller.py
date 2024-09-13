class PID_Controller(object):
    """docstring for PID_Controller."""

    def __init__(self, values, output_min, output_max):
        self.kp = values[1]  # Proportional gain
        self.ki = values[2]  # Integral gain
        self.kd = values[3]  # Derivative gain
        self.setpoint = values[0]  # Desired value
        self.output_min = output_min
        self.output_max = output_max

        # Initialize error terms
        self._prev_error = 0
        self._integral = 0



    def reset(self):
        self.update_pid(0, 0, 0, 0)
        self._prev_error = 0
        self._integral = 0



    def update_pid(self, values):
        self.kp = values[1]  # Proportional gain
        self.ki = values[2]  # Integral gain
        self.kd = values[3]  # Derivative gain
        self.setpoint = values[0]  # Desired value


    def calc(self, current_value, dt):
        # Calculate the error
        error = self.setpoint - current_value

        # Proportional term
        p = self.kp * error

        # Integral term
        self._integral += error * dt
        i = self.ki * self._integral

        # Derivative term
        derivative = (error - self._prev_error) / dt
        d = self.kd * derivative

        # Update previous error
        self._prev_error = error

        # Calculate the PID output
        output = p + i + d
        # output = max(self.output_min, min(self.output_max, output))

        # print(f"Output:{output}")
        return {
            "P":p,
            "I":i,
            "D":d,
            "output":output,
            "error": error
        }

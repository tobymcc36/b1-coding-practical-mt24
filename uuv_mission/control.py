class PIDController:
    def __init__(self, KP, KI, KD, integral_limit):
        self.KP = KP
        self.KD = KD
        self.KI = KI
        self.prev_error = 0.0
        self.integral = 0.0
        self.integral_limit = integral_limit

    def reset(self):
        self.prev_error = 0.0
        self.integral = 0.0

    def compute_control(self, reference, measurement):
        error = reference - measurement
        self.integral += error

        if self.integral_limit is not None:
            self.integral = max(min(self.integral, self.integral_limit), -self.integral_limit)

        derivative = error - self.prev_error
        control = self.KP * error + self.KI * self.integral + self.KD * derivative
        self.prev_error = error
        return control

    def __call__(self, reference, measurement):
        return self.compute_control(reference, measurement)
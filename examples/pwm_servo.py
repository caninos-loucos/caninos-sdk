from caninos_sdk.labrador import Labrador
import sys, timeit

labrador = Labrador()

if len(sys.argv) < 2:
    raise "Please provide the following parameter: degrees"

degrees = int(sys.argv[1])


def toDuty(degree):
    # config for motor SG90
    duty = degree / 18
    return (duty + 2) / 100


frequency = 50
duty = toDuty(degrees)
print(duty)
labrador.pin11.enable_pwm(alias="motor1", freq=frequency, duty_cycle=duty)
start = timeit.default_timer()
passed_time = timeit.default_timer() - start
labrador.motor1.pwm.start()
print((20 / frequency))
while passed_time < (20 / frequency):
    passed_time = timeit.default_timer() - start
labrador.motor1.pwm.stop()
print(passed_time)

class HourlyPaidEmployee:
 def __init__(self, hours_worked, extra_hours_worked):
  self.hours_worked = hours_worked
  self.extra_hours_worked = extra_hours_worked
  self.payment_per_hour = 75
  self.idle_hours_per_day = 8
  self.idle_payment = 1500

 def calculate_gross_pay(self):
  total_hours_worked = self.hours_worked + self.extra_hours_worked
  if total_hours_worked <= self.idle_hours_per_day:
   gross_pay = total_hours_worked * self.payment_per_hour
  else:
   idle_payment = self.idle_payment
   extra_hours_payment = (total_hours_worked - self.idle_hours_per_day) * self.payment_per_hour
   gross_pay = idle_payment + extra_hours_payment
  return gross_pay


hours_worked = int(input("Enter the number of hours worked: "))
extra_hours_worked = int(input("Enter the number of extra hours worked: "))

employee = HourlyPaidEmployee(hours_worked, extra_hours_worked)

gross_pay = employee.calculate_gross_pay()
print("Gross Pay: Rs.", gross_pay)

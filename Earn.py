print "How much do you make Bi-weekly?",
Bi_weekly = float(raw_input ())
print "How many hours of OT did you work this pay period?",
period_OT = float(raw_input ())
print "How much do you earn per hour for OT?",
OT_earnings = float(raw_input ())

print "So you'll get paid %r this pay period" % float(Bi_weekly + (period_OT * OT_earnings))

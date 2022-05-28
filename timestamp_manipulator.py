#please do not bother commenting on this solution, it's bad I know, in the future something more convenient would be implemented
#it is just to reduce api invocations
class Timestamp:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.time = timestamp.split('T')[1]
        self.hours = self.time[0:2]
        self.minutes = self.time[3:5]
        self.seconds = self.time[6:8]
        self.new_minutes = 0
        self.new_hour = 0

    def adjust_timestamp(self):
        new_seconds = int(self.seconds) + 1

        if new_seconds < 10:
            return self.hours + ':' + self.minutes + ':' + '0' + str(new_seconds) + 'Z'
        elif new_seconds == 60:
            new_minutes = int(self.minutes) + 1
            if new_minutes < 10:
                new_minutes = '0' + str(new_minutes)
                return self.hours + ':' + new_minutes + ':' + '00Z'
            elif new_minutes == 60:
                new_hour = int(self.hours) + 1
                if new_hour < 10:
                    return '0' + str(new_hour) + ':00:' + '00Z'
                elif new_hour < 24:
                    return str(new_hour) + ':00:' + '00Z'
                else:
                    return self.hours + ':' + self.minutes + ':' + self.seconds + 'Z'
            else:
                return self.hours + ':' + str(new_minutes) + ':00Z'
        else:
            return self.hours + ':' + self.minutes + ':' + str(new_seconds) + 'Z'

    def get_new_timestamp(self):
        new_timestamp = self.adjust_timestamp()
        result = self.timestamp.replace(self.time, new_timestamp)
        return result

stamp = Timestamp('2022-05-15T22:14:14Z')
new = stamp.get_new_timestamp()
print(new)
import  weather_pb2 as pb

message = pb.Temperature(station='s42', value=17.2)

message.time.GetCurrentTime()
print(message)

data = message.SerializeToString()
print(data)

message2 = pb.Temperature.FromString(data)
print(message2)

# GRPC https://www.linkedin.com/learning/effective-serialization-with-python/grpc?contextUrn=urn%3Ali%3AlearningCollection%3A6831514532045701120&u=2113185
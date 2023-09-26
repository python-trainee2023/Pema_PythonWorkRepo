# class FileManger:
#     def __int__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#         def __enter__ (self):
#             self.file = open (self.filename, self.mode)
#             return self.file
#         def __exit__(self, exc_type, exc_value, exc_traceback)
#             self.file.close()
#     with FileManger("test.txt", "w") as f:
#              f.write("This is test file")
#
#                 print(f.closed)
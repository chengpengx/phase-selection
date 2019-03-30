 1 class Config(object):
  2   def __init__(self):
  3     self.learning_rate = 0.0001
  4     self.batch_size = 512
  5     self.win_size = 400
  6     self.n_traces = 1
  7     self.display_step = 50
  8     self.n_threads = 2
  9     self.n_epochs = None
 10     self.regularization = 1e-3
 11     self.n_clusters = None
 12
 13     # Number of epochs, None is infinite
 14     n_epochs = None
~

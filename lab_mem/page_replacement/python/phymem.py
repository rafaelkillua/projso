# This is the only file you must implement

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you which

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

from random import randint

def SelectAlgorithm(algorithm):
  return globals()[algorithm]()

"""How many bits to use for the Aging algorithm"""
ALGORITHM_AGING_NBITS = 8

class PhysicalMemory:

  def __init__(self, algorithm):
    assert algorithm in {"fifo", "nru", "aging", "second-chance"}
    self.algorithm = SelectAlgorithm(algorithm.replace("-", "").upper())

  def put(self, frameId):
    """Allocates this frameId for some page"""
    # Notice that in the physical memory we don't care about the pageId, we only
    # care about the fact we were requested to allocate a certain frameId
    self.algorithm.put(frameId)

  def evict(self):
    """Deallocates a frame from the physical memory and returns its frameId"""
    # You may assume the physical memory is FULL so we need space!
    # Your code must decide which frame to return, according to the algorithm
    return self.algorithm.evict()

  def clock(self):
    """The amount of time we set for the clock has passed, so this is called"""
    # Clear the reference bits (and/or whatever else you think you must do...)
    self.algorithm.clock()

  def access(self, frameId, isWrite):
    """A frameId was accessed for read/write (if write, isWrite=True)"""
    self.algorithm.access(frameId, isWrite)
    
  def printMe(self):
    self.algorithm.printMe()

class FIFO:
  def __init__(self):
    # List of frameId
    self.allocatedFrames = []

  def put(self, frameId):
    self.allocatedFrames.append(frameId)

  def evict(self):
    # Selects oldest frame (first in queue)
    return self.allocatedFrames.pop(0)

  def clock(self):
    # No need
    pass

  def access(self, frameId, isWrite):
    # No need
    pass

  def printMe(self):
    print (self.allocatedFrames)

class NRU:
  def __init__(self):
    self.allocatedFrames = {}

  def put(self, frameId):
    # Dict of frameId: (bitR, bitM)
    self.allocatedFrames[frameId] = [0, 0]

  def evict(self):
    # Get all frames in lower classes and random to select one of them
    frames = self._get_all_from_class(self._get_lowest_class())
    random_index = randint(0, len(frames) - 1)
    self.allocatedFrames.pop(frames[random_index])
    return frames[random_index]

  def clock(self):
    # Resetting all frames' bitR
    for value in self.allocatedFrames.values():
      value[0] = 0

  def access(self, frameId, isWrite):
    # Put 1 on bitR (accessed), put 1 on bitM if modified (write)
    self.allocatedFrames[frameId][0] = 1
    if (isWrite):
      self.allocatedFrames[frameId][1] = 1

  def _get_class(self, frame):
    # Get frame's class
    i = frame[0]
    i = i << 1
    return i + frame[1]

  def _get_lowest_class(self):
    # Get lowest class on allocated frames, to know from which class remove the frame
    lowest = 4
    for value in self.allocatedFrames.values():
      actual = self._get_class(value)
      if (actual < lowest):
        lowest = actual
    return lowest

  def _get_all_from_class(self, classNumber):
    # Get all frames from given class
    frames = []
    bitR, bitM = 0, '{0:02b}'.format(classNumber)[1]
    if (classNumber > 1):
      bitR = '{0:02b}'.format(classNumber)[0]
    for key, value in self.allocatedFrames.items():
      if (value[0] == int(bitR) and value[1] == int(bitM)):
        frames.append(key)
    return frames

  def printMe(self):
    print (self.allocatedFrames)

class AGING:
  def __init__(self):
    self.allocatedFrames = {}

  def put(self, frameId):
    # Dict of frameId: counter
    self.allocatedFrames[frameId] = 0

  def evict(self):
    # Get the frame with lowest counter
    minFrame = min(self.allocatedFrames, key=self.allocatedFrames.get)
    self.allocatedFrames.pop(minFrame)
    return minFrame

  def clock(self):
    # When clock ticks, shift everybody to the right
    for key, value in self.allocatedFrames.items():
      self.allocatedFrames[key] = value >> 1


  def access(self, frameId, isWrite):
    # Add the reference bit (1) to the left of the counter. Doesn't care if isWrite
    self.allocatedFrames[frameId] = 1 << (ALGORITHM_AGING_NBITS - 1) | self.allocatedFrames[frameId]

  def printMe(self):
    print (self.allocatedFrames)

class SECONDCHANCE:
  def __init__(self):
    self.allocatedFrames = []

  def put(self, frameId):
    # List of [frameId, bitR]
    self.allocatedFrames.append([frameId, 0])

  def evict(self):
    # While bitR != 0, put it on 0 and move page to end of queue. Then, return the next bitR = 0
    while (self.allocatedFrames[0][1] != 0):
      self.allocatedFrames[0][1] = 0
      self.allocatedFrames.append(self.allocatedFrames.pop(0))
    return self.allocatedFrames.pop(0)[0]

  def clock(self):
    # DOUBT: When clock ticks, does the bitR get restarted?
    for frame in self.allocatedFrames:
      frame[1] = 0

  def access(self, frameId, isWrite):
    # This algorithm doesn't care about writing
    for frame in self.allocatedFrames:
      if (frame[0] == frameId):
        frame[1] = 1
        
  def printMe(self):
    print (self.allocatedFrames)

if __name__ == '__main__':
  #phy = PhysicalMemory("fifo")
  #phy = PhysicalMemory("nru")
  #phy = PhysicalMemory("second-chance")
  phy = PhysicalMemory("aging")
  phy.put(1)
  phy.put(2)
  phy.put(3)
  phy.put(4)
  phy.put(5)
  phy.put(6)
  phy.put(7)
  phy.put(8)
  phy.access(1, False)
  phy.access(2, True)
  phy.access(3, False)
  phy.access(4, True)
  phy.clock()
  phy.access(5, False)
  phy.access(6, True)
  phy.access(2, False)
  phy.printMe()
  print(phy.evict())
  phy.printMe()
  print(phy.evict())
  phy.printMe()
  print(phy.evict())
  phy.printMe()
  print(phy.evict())
  phy.printMe()
  print(phy.evict())
  phy.printMe()
  print(phy.evict())
  phy.printMe()
  print(phy.evict())
  phy.printMe()
  print(phy.evict())
  phy.printMe()
class PrimitiveTypes:
  @staticmethod
  def count_num_bits(number: int) -> int:
      """
      Counts the number of bits on an integer
      """
      count = 0
      while number:
          count += 1
          number >>= 1
      return count

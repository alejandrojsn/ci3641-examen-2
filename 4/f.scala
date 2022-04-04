import scala.collection.mutable.ArrayDeque

def tailf(n: Int, a0: Long, a1: Long, a2: Long, a3: Long, a4: Long, a5: Long, a6: Long, a7: Long, a8: Long, a9: Long, a10: Long, a11: Long): Long = n match {
  case 0 => a0
  case 1 => a1
  case 2 => a2
  case 3 => a3
  case 4 => a4
  case 5 => a5
  case 6 => a6
  case 7 => a7
  case 8 => a8
  case 9 => a9
  case 10 => a10
  case 11 => a11
  case n => tailf(n - 1, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a0 + a3 + a6 + a9)
}

def recf(n: Long): Long = n match {
  case n if 0L until 12L contains n => n
  case n => recf(n-3L) + recf(n-6L) + recf(n-9L) + recf(n-12L)
}

def itf(n: Int): Long = {
  if (n < 12) return n
  var q = new ArrayDeque(12).addAll(List(0L, 1L, 2L, 3L, 4L, 5L, 6L, 7L, 8L, 9L, 10L, 11L))
  for (i <- 12 to n) {
    val x = q(0) + q(3) + q(6) + q(9)
    q = q.addOne(x)
    q.removeHead()
  }
  return q.removeLast()
}

object Main extends App {
  println("iterativo:")
  for (i <- 0 to 198 by 18) {
    val start = System.nanoTime
    val result = itf(i)
    val duration = (System.nanoTime - start) / 1e6d

    println(s"$i: $result (${f"$duration%1.14f"} s)")
  }
  println("recursivo de cola:")
  for (i <- 0 to 198 by 18) {
    val start = System.nanoTime
    val result = tailf(i, 0L, 1L, 2L, 3L, 4L, 5L, 6L, 7L, 8L, 9L, 10L, 11L)
    val duration = (System.nanoTime - start) / 1e6d

    println(s"$i: $result (${f"$duration%1.14f"} s)")
  }
  println("recursivo:")
  for (i <- 0 to 198 by 18) {
    val start = System.nanoTime
    val result = recf(i)
    val duration = (System.nanoTime - start) / 1e6d

    println(s"$i: $result (${f"$duration%1.14f"} s)")
  }
}

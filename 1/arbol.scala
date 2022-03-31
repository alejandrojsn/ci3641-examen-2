import Arbol._
import scala.math.Ordering.Implicits._

sealed abstract class Arbol[T: Ordering](val v: T);

case class Hoja[T: Ordering](override val v: T) extends Arbol[T](v);

case class Rama[T: Ordering](override val v: T, val i: Arbol[T], val d: Arbol[T]) extends Arbol[T](v);

object Arbol {
  def esMinHeapBalanceado[T: Ordering](a: Arbol[T]): Boolean = {
    def _esMinHeapBalanceado[T: Ordering](a: Arbol[T]): (Boolean, Int) = a match {
      case Hoja(_) => (true, 0)
      case Rama(v, i, d) => {
        val (esHeapI, profundidadI) = _esMinHeapBalanceado(i)
        val (esHeapD, profundidadD) = _esMinHeapBalanceado(d)
        (v <= i.v && v <= d.v && esHeapI && esHeapD && (profundidadI - profundidadD).abs <=1, profundidadI.max(profundidadD) + 1)
      }
    }
    _esMinHeapBalanceado(a)._1
  }
}

object Main extends App {
  println(
    esMinHeapBalanceado(
      new Rama(
        0,
        new Rama(
          1,
          new Hoja(2),
          new Rama(
            2,
            new Hoja(3),
            new Hoja(3)
          )
        ),
        new Hoja(1)
      )
    )
  )
}

import Church._

sealed abstract class Church() {
  override def toString(): String = s"${toInt()}"
  def toInt(): Int
  def +(that: Church): Church
  def *(that: Church): Church
}

case object Zero extends Church {
  def toInt(): Int = 0
  def +(that: Church): Church = that
  def *(that: Church): Church = this
}

final case class Suc(val pred: Church) extends Church {
  def toInt(): Int = pred.toInt() + 1
  def +(that: Church): Church = that match {
    case Zero => this
    case Suc(pred) => suc(this + pred)
  }
  def *(that: Church): Church = that match {
    case Zero => Zero
    case Suc(pred) => this + this * pred
  }
}

object Church {
  def suc(x: Church): Church = new Suc(x)
  val from = {
    def _from(k: Church)(x: Int): Church = x match {
      case 0 => k
      case _ => _from(suc(k))(x-1)
    }
    _from(Zero)
  }
}

object Main extends App {
  val x = from(42)
  val y = from(69)
  
  println(x + y) // 111
  println(x * y) // 2898
}
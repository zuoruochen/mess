
val restaurant = List("谷田稻香","杨铭宇黄焖鸡米饭","东北水饺","易食汇","好粥道","桂林米粉","牛丼","石锅拌饭","兰州拉面")

def whereToEat(target :List[String]):String = {
  val index = scala.util.Random.nextInt(target.length)
  return target(index)
}

println(whereToEat(restaurant))

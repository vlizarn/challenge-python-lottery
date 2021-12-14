import data.lottery as Class

class Game(Class.Lottery):

    def __init__(
            self,
            lTitle = "Default",
            lTimes = 5,
            lTimesConjunt = 7,
            lTimesStar = 3,
            lMaxConjunt = 50,
            lMaxStar = 9,
            lRandConjunt = False,
            lRandStar = False
        ):
        super().__init_subclass__(
            lTitle,
            lTimes,
            lTimesConjunt,
            lTimesStar,
            lMaxConjunt,
            lMaxStar,
            lRandConjunt,
            lRandStar
        )

    def __del__(self) -> None:
        super().__del__()
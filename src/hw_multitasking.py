import asyncio
from datetime import datetime
from random import choice, randint

AVERAGE_LAP = 10
HORSES_COUNT = 9
RACE_COUNT = 10


def horse_name() -> str:
    tokens = {
        "first": ['a', 'ba', 'bo', 'bu', 'ce', 'cu', 'du', 'di', 'e', 'mu', 'me', 'oi', 'pi', 'xi', 'fu', 'ska', 'to',
                  'u', 'e', 'ste', 'spi', 'wo'],
        "midle": ['ka', 'ko', 'lo', 'pi', 'ro', 'go', 'la', 'si', 'ne', 'su', 'ni', 'ca', 'lu', 'ste', 'ri', 've', 'hu',
                  'cho', 'tu', 'i', 'gru'],
        "last": ['rat', 'cin', 'dur', 'zen', 'kut', 'vaz', 'don', 'lap', 'tin', 'zak', 'cup', 'don', 'tak', 'pin', 'in',
                 'tok', 'ak', 'al', 'duc']
    }
    parts = []
    parts.append(choice(tokens["first"]))
    for _ in range(randint(0, 2)):
        parts.append(choice(tokens["midle"]))
    parts.append(choice(tokens["last"]))
    return ''.join(parts).capitalize()


async def run_horse(name: str, coef: int) -> None:
    sign = 1 if randint(0, 99) < 90 else -1
    horse_time = AVERAGE_LAP + (randint(0, coef) * sign)

    print("Horse : {:<11} : Start  : {:<15}".format(name, str(datetime.now().time())))
    await asyncio.sleep(horse_time / 2)
    print("Horse : {:<11} : Lap    : {:<15}".format(name, str(datetime.now().time())))
    await asyncio.sleep(horse_time / 2)
    print("Horse : {:<11} : Finish : {:<15}".format(name, str(datetime.now().time())))


async def main():
    horses = [(horse_name(), randint(0, 4)) for horse in range(HORSES_COUNT)]
    print("Competitors:")
    [print(f"{idx + 1}. {horse[0]}") for idx, horse in enumerate(horses)]
    print("\nRace started!")

    for race in range(RACE_COUNT):
        print(f"Race #{race + 1}")
        tasks = [run_horse(*horse) for horse in horses]
        await asyncio.gather(*tasks)

    print("\nRace completed!")


if __name__ == "__main__":
    asyncio.run(main())

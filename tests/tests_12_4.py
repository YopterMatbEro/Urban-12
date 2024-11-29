import logging
from datetime import datetime as dt
from module_12_4 import Runner
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename=f'../logs/{dt.now().strftime("%Y-%m-%d %H-%M")}.log',
                    encoding='utf-8', format='\n%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            walker = Runner('Zombie', -7)
            logging.info('Успешно создан объект Runner')
            for _ in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        except ValueError:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)
        except Exception as e:
            logging.error(f'Непредвиденная ошибка: {e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            forest = Runner(3.14, 10)
            for _ in range(10):
                forest.run()
            self.assertEqual(forest.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        except ValueError:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)
        except Exception as e:
            logging.error(f'Непредвиденная ошибка: {e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        bolt = Runner('Usain Bolt')
        gepard = Runner('Just_gepard')

        for _ in range(10):
            bolt.walk()
            gepard.run()

        self.assertNotEqual(bolt.distance, gepard.distance)


if __name__ == '__main__':
    unittest.main()

def gcd_range(L, R):
    if L == R:
        return abs(L)
    else:
        return 1

def get_user_input():
    while True:
        try:
            L = int(input("Введите L (левая граница): "))
            R = int(input("Введите R (правая граница): "))
            
            if L > R:
                print("Ошибка: L не может быть больше R! Введите числа еще раз.")
                continue
            return L, R

        except ValueError:
            print("Ошибка: Пожалуйста, введите целые числа!")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            exit()
        except Exception as e:
            print(f"Ошибка: {e}")

def main():
    L, R = get_user_input()
    result = gcd_range(L, R)
    print(f"НОД всех чисел в диапазоне: {result}")
        
if __name__ == "__main__":
    main()

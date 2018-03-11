try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数： "))

    # 使用8除以用户的整数并输出
    result = 8 / num

    print(result)
except ZeroDivisionError:
    print("除0错误")

except ValueError:
    print("只能输入数字")

except Exception as result:
    print("未知错误 %s" % result)

else:
    print("Try成功")

finally:
    print('有没有错我都回执行')



from bbdata.routes.output import output

if __name__ == '__main__':
    output.login()

    test = output.values.get(
        "10622,10637",
        "2019-10-22T19:00",
        "2019-10-22T19:01",
    ).to_dataframe()

    print(test)


from bbdata.routes.output import output
if __name__ == '__main__':
    output.login()

    test = output.values.get(
        "10622,10639",
        "2019-10-22T19:00",
        "2019-10-22T19:01",
    )

    df = test.to_dataframe()

    test.to_csv("fuckers")
salaries = {
    "sales": [
        {
            "name": "Alice",
            "salary": 10000,
        },
        {
            "name": "Bob",
            "salary": 8950,
        },
    ],
    "development": {
        "frontend": [
            {
                "name": "Peter",
                "salary": 6500,
            },
            {
                "name": "Alex",
                "salary": 8300,
            },
        ],
        "backend": [
            {
                "name": "Pavel",
                "salary": 6500,
            },
        ]
    }
}


def sum_salaries(department: dict) -> int:
    if isinstance(department, list):
        return sum(person["salary"] for person in department)
    return sum(sum_salaries(dep) for dep in department.values())


if __name__ == '__main__':
    print(sum_salaries(salaries))

# earnings-calendar

Earnings dates for a given company.

`GET /api/earnings/{symbol}`

Query Parameters
- `last`: Optional (Number) - Number of quarters to return. Default is 1.

JSON Response [/api/earnings/AAPL?last=4](https://earningsapi.herokuapp.com/api/earnings/AAPL?last=4)
```json
["2019-07-31","2019-05-01","2019-01-30","2018-11-02"]
```

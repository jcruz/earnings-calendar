# earnings-calendar

Earnings dates for a given company.

`GET /api/earnings/{symbol}`

Query Parameters
- `last`: Optional (Number) - Number of quarters to return. Default is 1.

JSON Response [/api/earnings/AAPL?last=4](https://earningsapi.herokuapp.com/api/earnings/AAPL?last=4)
```json
["2019-07-30","2019-04-30","2019-01-29","2018-11-01"]
```

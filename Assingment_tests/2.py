# The launch game request from the casino:
{
  "casino_id": "casino",
  "game": "softswiss:CherryFiesta",
  "currency": "EUR",
  "locale": "de",
  "ipa": "46.53.162.55",
  "balance": 25000,
  "client_type": "desktop",
  "urls": {
    "deposit_url": "https://example.com/deposit",
    "return_url": "https://example.com"
  },

  "user": {
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "firstname": "John",
    "lastname": "Doe",
    "nickname": "spinmaster",
    "city": "Berlin",
    "country": "DE",
    "date_of_birth: "1980-12-26",
    "gender": "m",
    "registered_at": "2018-10-11"
  }
}

# Response from our server:

{"code":153,"message":"country is not allowed: DE"}



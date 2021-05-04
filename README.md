# Test for ProtoBuf for Kafka

## Producer

```
pip install -r requirements.txt
python produce-meals.py
```
There's no output. It just created a pizza with 2 drinks.

## Consumer

```
npm install
node consume-meals.js
```

@kafkajs/confluent-schema-registry v2.0.1 is buggy:
```
{
  decodedKey: '2919a554-e8c8-40fb-b06a-5cd91214f545',
  decodedValue: MealItems { itemName: 'pizza' }
}
```

while patched with https://github.com/kafkajs/confluent-schema-registry/pull/113
results in a much better:
```
{
  decodedKey: '35b201b1-47ee-4f7f-a2cc-433a06f7c02e',
  decodedValue: Meal {
    item: [],
    drink: [ [DrinkItems], [DrinkItems] ],
    name: 'pizza'
  }
}
```
Not perfect (I think), but much better.



// Use with https://docs.confluent.io/platform/current/quickstart/cos-docker-quickstart.html
// And its users producer

const { Kafka } = require('kafkajs')
const { SchemaRegistry } = require('@kafkajs/confluent-schema-registry')

const kafka = new Kafka({ clientId: 'my-app', brokers: ['t620.lan:9092'] })
const registry = new SchemaRegistry({ host: 'http://t620.lan:8081/' })
const consumer = kafka.consumer({ groupId: 'test12-group' })

const run = async () => {
  await consumer.connect()
  await consumer.subscribe({ topic: 'meal', fromBeginning: true })

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      // const decodedKey = await registry.decode(message.key)
      const decodedKey = message.key.toString();
      const decodedValue = await registry.decode(message.value)
      console.log({ decodedKey, decodedValue })
      console.log(`message=${JSON.stringify(message)}`)
    },
  })
}

run().catch(console.error)

console.log('Loading function');

const doc = require('node_modules/dynamodb-doc');

const dynamo = new doc.DynamoDB();


/**
 * Provide an event that contains the following keys:
 *
 *   - operation: one of the operations in the switch statement below
 *   - tableName: required for operations that interact with DynamoDB
 *   - payload: a parameter to pass to the operation being performed
 */
exports.handler = async (event) => {
    //console.log('Received event:', JSON.stringify(event, null, 2));

    const operation = event.operation;
    const payload = event.payload;

    if (event.tableName) {
        payload.TableName = event.tableName;
    }

    switch (operation) {
        case 'create':
            return await dynamo.putItem(payload).promise();
        case 'read':
            return await dynamo.getItem(payload).promise();
        case 'update':
            return await dynamo.updateItem(payload).promise();
        case 'delete':
            return await dynamo.deleteItem(payload).promise();
        case 'list':
            return await dynamo.scan(payload).promise();
        case 'echo':
            return payload;
        case 'ping':
            return 'pong';
        default:
            throw new Error(`Unrecognized operation "${operation}"`);
    }
};

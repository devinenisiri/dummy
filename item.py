import sqlite3
from flask_restful import Resource, request
from flask import render_template


class Item(Resource):
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1], 'category': row[2], 'used_for': row[3]}}
        return {'message': 'item not found'}
       

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'price': data['price'], 'category': data['category'], 'used_for': 10}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO items VALUES (?,?,?,?)"
        cursor.execute(query, (item['name'], item['price'], item['category'], item['used_for']))

        connection.commit()
        connection.close()
        
        return item

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "DELETE FROM items"
        cursor.execute(query)

        connection.commit()
        connection.close()
        
        return {'message': 'Item deleted'}

    def put(self, name):
        data = request.get_json()
        item = {'name': name, 'price':data['price'], 'category': 'category', 'used_for': 10}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'],  item['name']))

        connection.commit()
        connection.close()
        
        if item is None:
            items.append(item)
        else:
            item.update(data)
        return item

class Items(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT *FROM items"
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1], 'category': row[2], 'used_for': row[3]})

        connection.close()
        
        return {'items': items}

    def delete(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "DELETE FROM items"
        cursor.execute(query)

        connection.commit()
        connection.close()
        
        return {'message': 'Item deleted'}

class Dummy(Resource):
    def get(self):
         return render_template('filename.html')





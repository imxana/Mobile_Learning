from flask import request, jsonify, g

qiniu_setting = {
    'access_key' : 'iQ3ndG5uRpwdeln_gcrH3iiZ7E3KbMdJVkdYV9Im',
    'secret_key' : 'AGsp6K7fu1NsH2DnsPi7hW3qa3JXb4dtfeGvkm-A',
    'bucket_name' : 'image',
    'bucket_domain' : 'https://oi3qt7c8d.qnssl.com/',
    'callbakUrl' : 'http://139.129.24.151/qiniu/upload',
    'callbackBody' : 'filename:$(fname)&filesize:$(fsize)'
}

def register(app):

    @app.route('/qiniu/upload', methods=['POST'])
    def image_upload():
        """
        'callbackBody':'filename=$(fname)&filesize=$(fsize)'
        """
        name = request.values.get('filename', '')

        if name == '':
            return jsonify({'code':0})
        url = qiniu_setting['bucket_domain'] + name

        # name existed
        resource = g.User.query.filter_by(name=request.form['name']).first()
        if not bool(resource):
            g.db.session.add(g.Resource(name, url, None))
            g.db.session.commit()
        
        return jsonify({
            'code': 1,
            'url': url
            })



    # @app.route('/image/query', methods=['GET'])
    # def image_query():
        # i_id = request.args.get('i_id', '')
        
        # 'empty'
        # if i_id == '':
            # return jsonify({'code':0})

        # err, res = sqlQ.id_search(i_id, table='ec_image')
        # if err:
            # return jsonify(error.imageNotExisted)

        # return jsonify({
            # 'code':1, 
            # 'i_id':res[0],
            # 'i_url':res[1]
            # })





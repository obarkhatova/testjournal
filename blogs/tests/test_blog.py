def test_get_blogs_list(admin):
    res = admin.get('api/blogs')
    k=1
    # assert res.status_code = 200
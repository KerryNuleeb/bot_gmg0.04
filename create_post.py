def create(group_id, message, vk, attachment=None):
    print('Делаю пост')
    vk.wall.post(owner_id=group_id, from_group=1, message=message, attachment=attachment)

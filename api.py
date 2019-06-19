import scraper

IG_URL = 'https://instagram.com/{}'


class IGUser(object):

    def __init__(self, user_data):
        self._user_data = user_data

    def get_bio(self):
        return self._user_data['biography']

    def get_num_followed(self):
        return self._user_data['edge_follow']

    def get_num_followers(self):
        return self._user_data['edge_followed_by']

    def is_verified(self):
        return self._user_data['is_verified']

    def get_profile_pic(self):
        return self._user_data['profile_pic_url']

    def get_profile_pic_hd(self):
        return self._user_data['profile_pic_url_hd']

    def get_id(self):
        return self._user_data['id']

    def get_username(self):
        return self._user_data['username']

    def get_full_name(self):
        return self._user_data['full_name']

    def get_highlight_reel_count(self):
        return self._user_data['highlight_reel_count']

    def get_facebook(self):
        return self._user_data['connected_fb_page']

    def get_timeline_media_count(self):
        return self._user_data['edge_owner_to_timeline_media']['count']

    def get_timeline_media(self):
        # We should do some data parsing here to clean it up a little bit
        edges = self._user_data['edge_owner_to_timeline_media']['edges']
        for k, v in enumerate(edges):
            edges[k] = v['node']
        return edges


# Function is dependent on the path to this object
# This will break if instagram changes its graph
def get_user(username):
    return IGUser(scraper.get_data(IG_URL.format(username))['entry_data']['ProfilePage'][0]['graphql']['user'])

import requests


class LolzApi:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://api.lolz.guru/'
        self.session = requests.Session()
        self.session.headers = {'Authorization': f'Bearer {self.token}'}

    def get_categories(self, parent_category_id=None, parent_forum_id=None, order=None):
        """
        List of all categories in the system.
        :param parent_category_id:
        :param parent_forum_id:
        :param order:
        :return:
        """
        data = {}
        if parent_category_id: data['parent_category_id'] = parent_category_id
        if parent_forum_id: data['parent_forum_id'] = parent_forum_id
        if order: data['order'] = order
        return self.session.get(
            self.base_url + f'/categories', data=data).json()

    def get_category_detail(self, categoryID):
        """
        Detail information of a category.
        :param categoryID:
        :return:
        """
        return self.session.get(self.base_url + f'/categories/{categoryID}').json()

    def get_forums(self, parent_category_id=None, parent_forum_id=None, order=None):
        """
        List of all forums in the system.
        :param parent_category_id:
        :param parent_forum_id:
        :param order:
        :return:
        """
        data = {}
        if parent_category_id: data['parent_category_id'] = parent_category_id
        if parent_forum_id: data['parent_forum_id'] = parent_forum_id
        if order: data['order'] = order
        return self.session.get(
            self.base_url + f'/forums', data=data).json()

    def get_forum_detail(self, forumID):
        """
        Detail information of a category.
        :param forumID:
        :return:
        """
        return self.session.get(self.base_url + f'/forums/{forumID}').json()

    def get_forum_follower(self, forumID):
        """
        List of a forum's followers. For privacy reason, only the current user will be included in the list
        (if the user follows the specified forum).
        Since forum-2014053001.
        :param forumID:
        :return:
        """
        return self.session.get(self.base_url + f'forums/{forumID}/followers').json()

    def follow_forum(self, forumID, post=None, alert=None, email=None):
        """
        Follow a forum
        :param forumID:
        :param post:
        :param alert:
        :param email:
        :return:
        """
        data = {}
        if post: data['post'] = post
        if alert: data['alert'] = alert
        if email: data['email'] = email
        return self.session.post(self.base_url + f'forums/{forumID}/followers', data=data).json()

    def unfollow_forum(self, forumID):
        """
        Un-follow a forum.
        :param forumID:
        :return:
        """
        return self.session.delete(self.base_url + f'/forums/{forumID}/followers').json()

    def get_list_follow(self, total=None):
        """
        List of followed forums by current user.
        Since forum-2014053001.
        :param total:
        :return:
        """
        data = {}
        if total: data['total'] = total
        return self.session.get(self.base_url + 'forums/followed', data=data).json()

    def get_pages(self, parent_page_id=None, order=None):
        """
        List of all pages in the system.
        Since forum-2015072302.
        :param parent_page_id:
        :param order:
        :return:
        """
        data = {}
        if parent_page_id: data['parent_page_id'] = parent_page_id
        if order: data['order'] = order
        return self.session.get(self.base_url + 'pages', data=data).json()

    def get_pages_detail(self, pageID):
        """
        Detail information of a page.
        Since forum-2015072302.
        :param pageID:
        :return:
        """
        return self.session.get(self.base_url + f'pages/{pageID}').json()

    def get_navigation(self, parent=None):
        """
        List of navigation elements within the system.
        Since forum-2015030601.
        :param parent:
        :return:
        """
        data = {}
        if parent: data['parent'] = parent
        return self.session.get(self.base_url + 'navigation', data=data).json()

    def get_threads(self, **kwargs):
        """
        List of threads in a forum (with pagination).
        :param forum_id:
        :param thread_ids:
        :param creator_user_id:
        :param sticky:
        :param thread_prefix_id:
        :param thread_tag_id:
        :param page:
        :param limit:
        :param order:
        :param thread_create_date:
        :param thread_update_date:
        :return:
        """
        data = kwargs
        print(data)
        return self.session.get(self.base_url + 'threads', data=data).json()

    def create_thread(self, forum_id, thread_title, post_body, thread_prefix_id=None, thread_tags=None):
        """
        Create a new thread.
        :param forum_id:
        :param thread_title:
        :param post_body:
        :param thread_prefix_id:
        :param thread_tags:
        :return:
        """
        data = {'forum_id': forum_id, 'thread_title': thread_title, 'post_body': post_body}
        if thread_prefix_id: data['thread_prefix_id'] = thread_prefix_id
        if thread_tags: data['thread_tags'] = thread_tags
        return self.session.post(self.base_url + 'threads', data=data).json()

    def thread_attachment(self, file, forum_id, attachment_hash=None):
        """
        Upload an attachment for a thread.
        :param file: binary file open('file', 'rb')
        :param forum_id:
        :param attachment_hash:
        :return:
        """
        data = {'file': file, 'forum_id': forum_id}
        if attachment_hash: data['attachment_hash'] = attachment_hash
        return self.session.post(self.base_url + 'threads/attachments', data=data).json()

    def del_thread_attachment(self, forum_id, attachment_id, attachment_hash=None):
        """
        Delete an attachment for a thread.
        :param forum_id:
        :param attachment_id:
        :param attachment_hash:
        :return:
        """
        data = {'forum_id': forum_id, 'attachment_id': attachment_id}
        if attachment_hash: data['attachment_hash'] = attachment_hash
        return self.session.delete(self.base_url + 'threads/attachments', data=data).json()

    def get_thread_detail(self, threadID):
        """
        Detail information of a thread.
        :param threadID:
        :return:
        """
        return self.session.get(self.base_url + f'threads/{threadID}').json()

    def delete_thread(self, threadID, reason=None):
        """
        Delete a thread.
        :param threadID:
        :param reason:
        :return:
        """
        data = {}
        if reason: data['reason'] = reason
        return self.session.delete(self.base_url + f'threads/{threadID}', data=data).json()

    def get_thread_followers(self, threadID):
        """
        List of a thread's followers.
        For privacy reason, only the current user will be included in the list (if the user follows the specified thread).
        The privacy change was put in place since forum-2014053001, earlier versions return all followers of the thread.
        :param threadID:
        :return:
        """
        return self.session.get(self.base_url + f'threads/{threadID}/followers').json()

    def follow_thread(self, threadID, email=None):
        """
        Follow a thread.
        :param threadID:
        :param email:
        :return:
        """
        data = {}
        if email: data['email'] = email
        return self.session.post(self.base_url + f'threads/{threadID}/followers', data=data).json()

    def unfollow_thread(self, threadID):
        """
        Un-follow a thread.
        :param threadID:
        :return:
        """
        return self.session.delete(self.base_url + f'threads/{threadID}/followers').json()

    def get_list_follow_thread(self, total=None):
        """
        List of followed threads by current user.
        Since forum-2014053002.
        :param total:
        :return:
        """
        data = {}
        if total: data['total'] = total
        return self.session.get(self.base_url + 'threads/followed', data=data).json()

    def get_list_navigation(self, threadID):
        """
        List of navigation elements to reach the specified thread.
        Since forum-2019052201.
        :param threadID:
        :return:
        """
        return self.session.get(self.base_url + f'threads/{threadID}/navigation').json()

    def get_poll_detail(self, threadID):
        """
        Detail information of a poll.
        Since forum-2020042601.
        :param threadID:
        :return:
        """
        return self.session.get(self.base_url + f'threads/{threadID}/poll').json()

    def vote_poll_thread(self, threadID, response_id, response_ids: tuple = None):
        """
        Vote on a thread poll.
        Since forum-2015100601.
        :param threadID:
        :param response_id:
        :param response_ids:
        :return:
        """
        data = {'response_id': response_id}
        if response_ids: data['response_ids'] = response_ids
        return self.session.post(self.base_url + f'threads/{threadID}/poll/votes', data=data).json()

    def get_new_threads(self, limit=None, forum_id=None, data_limit=None):
        """
        List of unread threads (must be logged in).
        :param limit:
        :param forum_id:
        :param data_limit:
        :return:
        """
        data = {}
        if limit: data['limit'] = limit
        if forum_id: data['forum_id'] = forum_id
        if data_limit: data['data_limit'] = data_limit
        return self.session.get(self.base_url + 'threads/new', data=data).json()

    def get_recent_threads(self, days=None, limit=None, forum_id=None, data_limit=None):
        """
        List of recent threads.
        :param days:
        :param limit:
        :param forum_id:
        :param data_limit:
        :return:
        """
        data = {}
        if days: data['days'] = days
        if limit: data['limit'] = limit
        if forum_id: data['forum_id'] = forum_id
        if data_limit: data['data_limit'] = data_limit
        return self.session.get(self.base_url + 'threads/recent', data=data).json()

    def get_posts_thread(self, thread_id, page_of_post_id=None, post_ids=None, page=None, limit=None, order=None):
        """
        List of posts in a thread (with pagination).
        :param thread_id:
        :param page_of_post_id:
        :param post_ids:
        :param page:
        :param limit:
        :param order:
        :return:
        """
        data = {}
        if thread_id: data['thread_id'] = thread_id
        if page_of_post_id: data['page_of_post_id'] = page_of_post_id
        if post_ids: data['post_ids'] = post_ids
        if page: data['page'] = page
        if limit: data['limit'] = limit
        if order: data['order'] = order
        return self.session.get(self.base_url + 'posts', data=data).json()

    def create_new_post(self, thread_id, quote_post_id=None, post_body=None):
        """
        Create a new post.
        :param thread_id:
        :param quote_post_id:
        :param post_body:
        :return:
        """
        data = {'thread_id': thread_id}
        if quote_post_id: data['quote_post_id'] = quote_post_id
        if post_body: data['post_body'] = post_body
        return self.session.post(self.base_url + 'posts', data=data).json()

    def upload_attachment_post(self, file, thread_id=None, post_id=None, attachment_hash=None):
        """
        Upload an attachment for a post.
        The attachment will be associated after the post is saved.
        :param file:
        :param thread_id:
        :param post_id:
        :param attachment_hash:
        :return:
        """
        data = {'file': file}
        if thread_id: data['thread_id'] = thread_id
        if post_id: data['post_id'] = post_id
        if attachment_hash: data['attachment_hash'] = attachment_hash
        return self.session.post(self.base_url + 'posts/attachments', data=data).json()

    def get_post_detail(self, postID):
        """
        Detail information of a post.
        :param postID:
        :return:
        """
        return self.session.get(self.base_url + f'posts/{postID}').json()

    def edit_post(self, postID, post_body, thread_title=None, thread_prefix_id=None, thread_tags=None,
                  thread_node_id=None):
        """
        Edit a post.
        :param postID:
        :param post_body:
        :param thread_title:
        :param thread_prefix_id:
        :param thread_tags:
        :param thread_node_id:
        :return:
        """
        data = {'post_body': post_body}
        if thread_title: data['thread_title'] = thread_title
        if thread_prefix_id: data['thread_prefix_id'] = thread_prefix_id
        if thread_tags: data['thread_tags'] = thread_tags
        if thread_node_id: data['thread_node_id'] = thread_node_id
        return self.session.put(self.base_url + f'posts/{postID}', data=data).json()

    def delete_post(self, postID, reason=None):
        """
        Delete a post.
        :param postID:
        :param reason:
        :return:
        """
        data = {}
        if reason: data['reason'] = reason
        return self.session.delete(self.base_url + f'posts/{postID}', data=data).json()

    def get_list_attachments_post(self, postID):
        """
        List of attachments of a post.
        :param postID:
        :return:
        """
        return self.session.get(self.base_url + f'posts/{postID}/attachments').json()

    def get_binary_attachments_post(self, postID, attachmentID, max_width=None, max_height=None, keep_ratio=None):
        """
        Binary data of a post's attachment.
        :param postID:
        :param attachmentID:
        :param max_width:
        :param max_height:
        :param keep_ratio:
        :return:
        """
        data = {}
        if max_width: data['max_width'] = max_width
        if max_height: data['max_height'] = max_height
        if keep_ratio: data['keep_ratio'] = keep_ratio
        return self.session.get(self.base_url + f'posts/{postID}/attachments/{attachmentID}', data=data).json()

    def delete_post_attachment(self, postID, attachmentID, thread_id=None, attachment_hash=None):
        """
        Delete a post's attachment.
        :param postID:
        :param attachmentID:
        :param thread_id:
        :param attachment_hash:
        :return:
        """
        data = {}
        if thread_id: data['thread_id'] = thread_id
        if attachment_hash: data['attachment_hash'] = attachment_hash
        return self.session.delete(self.base_url + f'posts/{postID}/attachments/{attachmentID}', data=data).json()

    def get_list_liked_post(self, postID, page=None, limit=None):
        """
        List of users who liked a post.
        :param postID:
        :param page:
        :param limit:
        :return:
        """
        data = {}
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.get(self.base_url + f'posts/{postID}/likes', data=data).json()

    def like_post(self, postID):
        """
        Like a post.
        :param postID:
        :return:
        """
        return self.session.post(self.base_url + f'posts/{postID}/likes').json()

    def unlike_post(self, postID):
        """
        Unlike a post.
        :param postID:
        :return:
        """
        return self.session.delete(self.base_url + f'posts/{postID}/likes').json()

    def report_post(self, postID, message):
        """
        Report a post.
        :param postID:
        :param message:
        :return:
        """
        data = {}
        if message: data['message'] = message
        return self.session.post(self.base_url + f'posts/{postID}/report', data=data).json()

    def get_list_comments(self, postID, before=None):
        """
        List of post comments in a thread (with pagination).
        :param postID:
        :param before: The time in milliseconds (e.g. 1652177794083) before last comment date
        :return:
        """
        data = {}
        if before: data['before'] = before
        return self.session.get(self.base_url + f'posts/{postID}/comments').json()

    def create_new_comment(self, postID, comment_body):
        """
        Create a new post comment.
        :param postID:
        :type postID:
        :param comment_body:
        :type comment_body:
        :return:
        :rtype: json
        """
        data = {'comment_body': comment_body}
        return self.session.post(self.base_url + f'posts/{postID}/comments', data=data).json()

    def get_popular_tags(self):
        """
        List of popular tags (no pagination).
        Since forum-2015091002.
        :return:
        """
        return self.session.get(self.base_url + 'tags').json()

    def get_list_tags(self):
        """
        List of tags.
        Since forum-2017111101.
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + 'tags/list').json()

    def get_list_tagged(self, tagID, page=None, limit=None):
        """
        List of tagged contents.
        Since forum-2017050201.
        :param tagID:
        :type tagID:
        :param page:
        :type page:
        :param limit:
        :type limit:
        :return:
        :rtype: json
        """
        data = {}
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.get(self.base_url + f'tags/{tagID}', data=data).json()

    def get_filtered_tags(self, tag):
        """
        Filtered list of tags.
        Since forum-2015091002.
        :param tag:
        :type tag:
        :return:
        :rtype: json
        """
        data = {'tag': tag}
        return self.session.get(self.base_url + 'tags/find', data=data).json()

    def get_users(self, page=None, limit=None):
        """
        List of users (with pagination).
        :param page:
        :type page:
        :param limit:
        :type limit:
        :return:
        :rtype: json
        """
        data = {}
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.get(self.base_url + 'users', data=data).json()

    def create_new_user(self, **kwargs):
        """
        Create a new user.
        :param user_email:
        :type user_email:
        :param username:
        :type username:
        :param password:
        :type password:
        :param password_algo:
        :type password_algo:
        :param user_dob_day:
        :type user_dob_day:
        :param user_dob_month:
        :type user_dob_month:
        :param user_dob_year:
        :type user_dob_year:
        :param fields:
        :type fields:
        :param client_id:
        :type client_id:
        :param extra_data:
        :type extra_data:
        :param extra_timestamp:
        :type extra_timestamp:
        :return:
        :rtype: json
        """
        data = kwargs
        return self.session.post(self.base_url + 'users', data=data).json()

    def get_user_fields(self):
        """
        List of user fields.
        Since forum-2017122801.
        :return:
        :rtype:
        """
        return self.session.get(self.base_url + 'users/fields').json()

    def get_filtered_users(self, username=None, user_email=None):
        """
        Filtered list of users by username or email.
        Since forum-2015030901.
        :param username:
        :type username:
        :param user_email:
        :type user_email:
        :return:
        :rtype:
        """
        data = {}
        if username: data['username'] = username
        if user_email: data['user_email'] = user_email
        return self.session.get(self.base_url + 'users/find', data=data).json()

    def get_user_detail(self, userID=None, shortLink=None):
        """
        Detail information of a user.
        :param userID:
        :type userID:
        :param shortLink:
        :type shortLink:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'users/{userID if userID else shortLink}').json()

    def edit_user(self, userID, **kwargs):
        """
        Edit a user.
        Since forum-2015041501.
        The introduction of this method makes POST /users/:userId/password deprecated.
        :param userID
        :type userID
        :param password:
        :type password:
        :param password_old:
        :type password_old:
        :param password_algo:
        :type password_algo:
        :param user_email:
        :type user_email:
        :param username:
        :type username:
        :param user_title:
        :type user_title:
        :param primary_group_id:
        :type primary_group_id:
        :param secondary_group_ids:
        :type secondary_group_ids:
        :param user_dob_day:
        :type user_dob_day:
        :param user_dob_year:
        :type user_dob_year:
        :param user_dob_month:
        :type user_dob_month:
        :param fields:
        :type fields:
        :return:
        :rtype: json
        """
        data = kwargs
        return self.session.put(self.base_url + f'users/{userID}', data=data).json()

    def password_reset(self, oauth_token, username=None, email=None):
        """
        Request a password reset via email.
        Since forum-2018060601.
        :param oauth_token:
        :type oauth_token:
        :param username:
        :type username:
        :param email:
        :type email:
        :return:
        :rtype: json
        """
        data = {'oauth_token': oauth_token}
        if username: data['username'] = username
        if email: data['email'] = email
        return self.session.post(self.base_url + 'lost-password', data=data).json()

    def upload_avatar(self, userID, avatar):
        """
        Upload avatar for a user.
        :param userID:
        :type userID:
        :param avatar:
        :type avatar:
        :return:
        :rtype: json
        """
        data = {'avatar': avatar}
        return self.session.post(self.base_url + f'users/{userID}/avatar', data=data).json()

    def delete_avatar(self, userID):
        """
        Delete avatar for a user.
        :param userID:
        :type userID:
        :return:
        :rtype: json
        """
        return self.session.delete(self.base_url + f'users/{userID}/avatar').json()

    def get_followers(self, userID, order=None, page=None, limit=None):
        """
        List of a user's followers
        :param userID:
        :type userID:
        :param order:
        :type order:
        :param page:
        :type page:
        :param limit:
        :type limit:
        :return:
        :rtype: json
        """
        data = {}
        if order: data['order'] = order
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.get(self.base_url + f'users/{userID}/followers', data=data).json()

    def follow_user(self, userID):
        """
        Follow a user.
        :param userID:
        :type userID:
        :return:
        :rtype: json
        """
        return self.session.post(self.base_url + f'users/{userID}/followers').json()

    def unfollow_user(self, userID):
        """
        Follow a user.
        :param userID:
        :type userID:
        :return:
        :rtype: json
        """
        return self.session.delete(self.base_url + f'users/{userID}/followers').json()

    def get_users_folowings(self, userID, order=None, page=None, limit=None):
        """
        List of users whom are followed by a user.
        :param userID:
        :type userID:
        :param order:
        :type order:
        :param page:
        :type page:
        :param limit:
        :type limit:
        :return:
        :rtype: json
        """
        data = {}
        if order: data['order'] = order
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.get(self.base_url + f'users/{userID}/followings', data=data).json()

    def get_ignored(self, total=None):
        """
        List of a ignored users of current user.
        Since forum-2015072303.
        :param total:
        :type total:
        :return:
        :rtype: json
        """
        data = {}
        if total: data['total'] = total
        return self.session.get(self.base_url + 'users/ignored', data=data).json()

    def ignore_user(self, userID):
        """
        Ignore a user.
        Since forum-2015072303.
        :param userID:
        :type userID:
        :return:
        :rtype: json
        """
        return self.session.post(self.base_url + f'users/{userID}/ignore').json()

    def stop_ignore(self, userID):
        """
        Stop ignoring a user.
        Since forum-2015072303.
        :param userID:
        :type userID:
        :return:
        :rtype: json
        """
        return self.session.delete(self.base_url + f'users/{userID}/ignore').json()

    def get_users_groups(self):
        """
        List of all user groups. Since forum-2014092301.
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + 'users/groups').json()

    def get_user_groups(self, userID):
        """
        List of a user's groups.
        Since forum-2014092301.
        :param userID:
        :type userID:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'users/{userID}/groups').json()

    def content_create_by_user(self, userID, page=None, limit=None):
        """
        List of contents created by user (with pagination).
        Since forum-2015042001.
        :param userID:
        :type userID:
        :param page:
        :type page:
        :param limit:
        :type limit:
        :return:
        :rtype: json
        """
        data = {}
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.get(self.base_url + f'users/{userID}/timeline', data=data).json()

    def create_profile_post(self, userID, post_body, status=None):
        """
        Create a new profile post on a user timeline.
        Since forum-2015042001.
        :param userID:
        :type userID:
        :param post_body:
        :type post_body:
        :param status:
        :type status:
        :return:
        :rtype: json
        """
        data = {'post_body': post_body}
        if status: data['status'] = status
        return self.session.post(self.base_url + f'users/{userID}/timeline', data=data).json()

    def get_profile_post_detail(self, profilePostID):
        """
        Detail information of a profile post.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'profile-posts/{profilePostID}').json()

    def edit_profile_post(self, profilePostID, post_body):
        """
        Edit a profile post.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :param post_body:
        :type post_body:
        :return:
        :rtype: json
        """
        return self.session.put(self.base_url, f'profile-posts/{profilePostID}', data={'post_body': post_body}).json()

    def delete_profile_post(self, profilePostID, reason=None):
        """
        Delete a profile post.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :param reason:
        :type reason:
        :return:
        :rtype: json
        """
        data = {}
        if reason: data['reason'] = reason
        return self.session.delete(self.base_url + f'profile-posts/{profilePostID}', data=data).json()

    def get_users_likes_profile_post(self, profilePostID):
        """
        List of users who liked a profile post.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'profile-posts/{profilePostID}/likes').json()

    def like_profile_post(self, profilePostID):
        """
        Like a profile post.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :return:
        :rtype: json
        """
        return self.session.post(self.base_url + f'profile-posts/{profilePostID}/likes').json()

    def unlike_profile_post(self, profilePostID):
        """
        Like a profile post.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :return:
        :rtype: json
        """
        return self.session.delete(self.base_url + f'profile-posts/{profilePostID}/likes').json()

    def list_comments_profile_post(self, profilePostID, before=None):
        """
        List of comments of a profile post.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :param before:
        :type before:
        :return:
        :rtype: json
        """
        data = {}
        if before: data['before'] = before
        return self.session.get(self.base_url + f'profile-posts/{profilePostID}/comments').json()

    def new_profile_post_comment(self, profilePostID, comment_body):
        """
        Create a new profile post comment.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :param comment_body:
        :type comment_body:
        :return:
        :rtype: json
        """
        return self.session.post(self.base_url + f'profile-posts/{profilePostID}/comments',
                                 data={'comment_body': comment_body}).json()

    def comment_profile_post_detail(self, profilePostID, commentID):
        """
        Detail information of a profile post comment.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :param commentID:
        :type commentID:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'profile-posts/{profilePostID}/comments/{commentID}').json()

    def delete_profile_post_comment(self, profilePostID, commentID):
        """
        Delete a profile post's comment.
        Since forum-2015042001.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :param commentID:
        :type commentID:
        :return:
        :rtype: json
        """
        return self.session.delete(self.base_url + f'profile-posts/{profilePostID}/comments/{commentID}').json()

    def report_profile_post(self, profilePostID, message):
        """
        Report a profile post.
        Since forum-2015042001.
        :param profilePostID:
        :type profilePostID:
        :param message:
        :type message:
        :return:
        :rtype: json
        """
        data = {'message': message}
        return self.session.post(self.base_url + f'profile-posts/{profilePostID}/report', data=data).json()

    def get_list_conservation(self, page=None, limit=None):
        """
        List of conversations (with pagination).
        :param page:
        :type page:
        :param limit:
        :type limit:
        :return:
        :rtype: json
        """
        data = {}
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.get(self.base_url + 'conversations', data=data).json()

    def get_conservation_detail(self, conversationID):
        """
        Detail information of a conversation.
        :param conversationID:
        :type conversationID:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'conversations/{conversationID}').json()

    def delete_conservation(self, conversationID):
        """
        Delete a conversation.
        :param conversationID:
        :type conversationID:
        :return:
        :rtype: json
        """
        return self.session.delete(self.base_url + f'conversations/{conversationID}').json()

    def upload_attachment_conservation(self, file, attachment_hash=None):
        """
        Upload an attachment for a conversation.
        Since forum-2014053003.
        :param file:
        :type file:
        :param attachment_hash:
        :type attachment_hash:
        :return:
        :rtype: json
        """
        data = {'file': file}
        if attachment_hash: data['attachment_hash'] = attachment_hash
        return self.session.post(self.base_url + 'conversations/attachments', data=data).json()

    def delete_attachment_conservation(self, attachment_id, attachment_hash=None):
        """
        Delete an attachment for a conversation.
        Since forum-2014053003.
        :param attachment_id:
        :type attachment_id:
        :param attachment_hash:
        :type attachment_hash:
        :return:
        :rtype: json
        """
        data = {'attachment_id': attachment_id}
        if attachment_hash: data['attachment_hash'] = attachment_hash
        return self.session.delete(self.base_url + 'conversations/attachments', data=data).json()

    def get_conservation_messages(self, conversation_id, page=None, limit=None, order=None, before=None, after=None):
        """
        List of messages in a conversation (with pagination).
        :param conversation_id:
        :type conversation_id:
        :param page:
        :type page:
        :param limit:
        :type limit:
        :param order:
        :type order:
        :param before:
        :type before:
        :param after:
        :type after:
        :return:
        :rtype: json
        """
        data = {}
        if page: data['page'] = page
        if limit: data['limit'] = limit
        if order: data['order'] = order
        if before: data['before'] = before
        if after: data['after'] = after
        return self.session.get(self.base_url + 'conversation-messages', data=data).json()

    def create_new_conservation(self, conversation_id, message_body):
        """
        Create a new conversation message.
        :param conversation_id:
        :type conversation_id:
        :param message_body:
        :type message_body:
        :return:
        :rtype: json
        """
        data = {
            'conversation_id': conversation_id, 'message_body': message_body
        }
        return self.session.post(self.base_url + 'conversation-messages', data=data).json()

    def upload_attachments_conservation_message(self, file, conversation_id=None, message_id=None,
                                                attachment_hash=None):
        """
        Upload an attachment for a message.
        The attachment will be associated after the message is saved.
        Since forum-2014053003.
        :param file:
        :type file:
        :param conversation_id:
        :type conversation_id:
        :param message_id:
        :type message_id:
        :param attachment_hash:
        :type attachment_hash:
        :return:
        :rtype: json
        """
        data = {'file': file}
        if conversation_id: data['conversation_id'] = conversation_id
        if message_id: data['message_id'] = message_id
        if attachment_hash: data['attachment_hash'] = attachment_hash
        return self.session.post(self.base_url + 'conversation-messages/attachments', data=data).json()

    def conservation_message_detail(self, messageID):
        """
        Detail information of a message.
        :param messageID:
        :type messageID:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'conversation-messages/{messageID}').json()

    def edit_conservation_message(self, messageID, message_body):
        """
        Edit a message.
        Since forum-2014053101.
        :param messageID:
        :type messageID:
        :param message_body:
        :type message_body:
        :return:
        :rtype: json
        """
        data = {
            'message_body': message_body
        }
        return self.session.put(self.base_url + f'conversation-messages/{messageID}', data=data).json()

    def delete_conservation_message(self, messageID):
        """
        Delete a message.
        :param messageID:
        :type messageID:
        :return:
        :rtype: json
        """
        return self.session.delete(self.base_url + f'conversation-messages/{messageID}').json()

    def get_list_attachments_message(self, messageID):
        """
        List of attachments of a message.
        Since forum-2014053003.
        :param messageID:
        :type messageID:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'conversation-messages/{messageID}/attachments').json()

    def binary_attachments_message(self, messageID, attachmentID, max_width=None, max_height=None, keep_ratio=None):
        """
        Binary data of a message's attachment.
        Since forum-2014053003.
        :param messageID:
        :type messageID:
        :param attachmentID:
        :type attachmentID:
        :param max_width:
        :type max_width:
        :param max_height:
        :type max_height:
        :param keep_ratio:
        :type keep_ratio:
        :return:
        :rtype: json
        """
        data = {}
        if max_width: data['max_width'] = max_width
        if max_height: data['max_height'] = max_height
        if keep_ratio: data['keep_ratio'] = keep_ratio
        return self.session.get(self.base_url + f'conversation-messages/{messageID}/attachments/{attachmentID}',
                                data=data).json()

    def delete_message_attachments(self, messageID, attachmentID, conversation_id=None, attachment_hash=None):
        """
        Delete a message's attachment.
        Since forum-2014053003.
        :param messageID:
        :type messageID:
        :param attachmentID:
        :type attachmentID:
        :param conversation_id:
        :type conversation_id:
        :param attachment_hash:
        :type attachment_hash:
        :return:
        :rtype: json
        """
        data = {}
        if conversation_id: data['conversation_id'] = conversation_id
        if attachment_hash: data['attachment_hash'] = attachment_hash
        return self.session.delete(self.base_url + f'conversation-messages/{messageID}/attachments/{attachmentID}',
                                   data=data).json()

    def report_conservation_message(self, messageID, message):
        """
        Report a message.
        Since forum-2015081101.
        :param messageID:
        :type messageID:
        :param message:
        :type message:
        :return:
        :rtype: json
        """
        data = {"message": message}
        return self.session.post(self.base_url + f'conversation-messages/{messageID}/report', data=data).json()

    def get_notifications(self):
        """
        List of notifications (both read and unread).
        Since forum-2014022602.
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + 'notifications').json()

    def get_notification_detail(self, notificationID):
        """
        Get associated content of notification.
        The response depends on the content type.
        Since forum-2015041001.
        :param notificationID:
        :type notificationID:
        :return:
        :rtype: json
        """
        return self.session.get(self.base_url + f'notifications/{notificationID}/content').json()

    def send_custom_alert(self, userid=None, username=None, message=None, message_html=None, notification_type=None,
                          extra_data=None):
        """
        Send a custom alert.
        Since forum-2019123001.
        :param userid:
        :type userid:
        :param username:
        :type username:
        :param message:
        :type message:
        :param message_html:
        :type message_html:
        :param notification_type:
        :type notification_type:
        :param extra_data:
        :type extra_data:
        :return:
        :rtype: json
        """
        data = {}
        if userid: data['user_id'] = userid
        if username: data['username'] = username
        if message: data['message'] = message
        if message_html: data['message_html'] = message_html
        if notification_type: data['notification_type'] = notification_type
        return self.session.post(self.base_url + 'notifications/custom', data=data).json()

    def read_notification(self, notification_id=None):
        """
        Mark single notification or all existing notifications read.
        Since forum-2021080600.
        :param notification_id:
        :type notification_id:
        :return:
        :rtype: json
        If notification_id is omitted, it's mark all existing notifications as read.
        """
        data = {}
        if notification_id: data['notification_id'] = notification_id
        return self.session.post(self.base_url + 'notifications/read', data=data).json()

    def search_content(self, q, tag=None, forum_id=None, user_id=None, page=None, limit=None):
        """
        Search for all supported contents.
        Since forum-2015042002.
        :param q:
        :type q:
        :param tag:
        :type tag:
        :param forum_id:
        :type forum_id:
        :param user_id:
        :type user_id:
        :param page:
        :type page:
        :param limit:
        :type limit:
        :return:
        :rtype: json
        """
        data = {'q': q}
        if tag: data['tag'] = tag
        if forum_id: data['forum_id'] = forum_id
        if user_id: data['user_id'] = user_id
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.post(self.base_url + 'search', data=data).json()

    def search_tag_content(self, tag, tags=None, page=None, limit=None):
        """
        Search for tagged contents.
        Since forum-2015091001.
        :param tag:
        :type tag:
        :param tags:
        :type tags:
        :param page:
        :type page:
        :param limit:
        :type limit:
        :return:
        :rtype:
        """
        data = {'tag': tag}
        if tags: data['tags'] = tags
        if page: data['page'] = page
        if limit: data['limit'] = limit
        return self.session.post(self.base_url + 'search/tagged', data=data).json()


if __name__ == '__main__':
    lzt = LolzApi('c77ec7db7b5e6555cdc27846b66510852afe2864')
    cat = lzt.create_conservation('1', 2, 4)
    print(cat)

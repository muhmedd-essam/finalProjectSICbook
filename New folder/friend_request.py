import json
class FriendRequest:
    def __init__(self, filename="friend_requests.json"):
        self.filename = filename
        self.friend_requests = self.load_friend_requests()

    def load_friend_requests(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_friend_requests(self):
        with open(self.filename, "w") as file:
            json.dump(self.friend_requests, file, indent=2)

    def send_friend_request(self, sender, receiver):
        # Check if the sender and receiver are the same user
        if sender == receiver:
            return False  # You can't send a request to yourself

        if receiver in self.friend_requests:
            # Check if the sender has already sent a request to this receiver
            for request in self.friend_requests[receiver]['pending']:
                if request['sender'] == sender:
                    return False  # Sender has already sent a request to this receiver

        if receiver not in self.friend_requests:
            self.friend_requests[receiver] = {'pending': [], 'accepted': []}
        self.friend_requests[receiver]['pending'].append({'sender': sender, 'receiver': receiver})
        self.save_friend_requests()
        return True  # Request sent successfully

    def accept_friend_request(self, sender, receiver):
        if receiver in self.friend_requests and 'pending' in self.friend_requests[receiver]:
            for request in self.friend_requests[receiver]['pending']:
                if request['sender'] == sender:
                    self.friend_requests[receiver]['pending'].remove(request)
                    if 'friends' not in self.friend_requests[receiver]:
                        self.friend_requests[receiver]['friends'] = []
                    self.friend_requests[receiver]['friends'].append(sender)
                    self.save_friend_requests()

                    # Now update the sender's friend list as well
                    if sender in self.friend_requests and 'friends' in self.friend_requests[sender]:
                        self.friend_requests[sender]['friends'].append(receiver)
                        self.save_friend_requests()

                    return True
        return False

    def get_pending_requests(self, user):
        if user in self.friend_requests:
            return self.friend_requests[user]['pending']
        return []

    def get_accepted_requests(self, user):
        if user in self.friend_requests:
            return self.friend_requests[user]['accepted']
        return []
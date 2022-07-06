class Friend {
  constructor(email) {
    this.email = email;
    this.friends = [];
  }

  addFriendship(friend) {
    this.friends.push(friend);
    friend.friends.push(this);
  }

  canBeConnected(friend) {
    function dfs(group, now) {
      if (now === friend) {
        return true;
      }

      for (let next of now.friends) {
        if (!group.includes(next.email)) {
          if (dfs([...group, next.email], next)) {
            return true;
          }
        }
      }

      return false;
    }
    return dfs([this], this);
  }

  canBeConnected(friend) {
    const candidates = [this];
    const group = [this.email];

    while (candidates.length > 0) {
      const nowFriend = candidates.shift();
      for (let nextFriend of nowFriend.friends) {
        if (nextFriend === friend) return true;
        if (!group.includes(nextFriend.email)) {
          group.push(nextFriend.email);
          candidates.push(nextFriend);
        }
      }
    }

    return false;
  }
}

const a = new Friend("A");
const b = new Friend("B");
const c = new Friend("C");
const d = new Friend("D");
const e = new Friend("E");
const f = new Friend("F");

a.addFriendship(b);
b.addFriendship(c);
c.addFriendship(d);
d.addFriendship(e);
c.addFriendship(f);

console.log(a.canBeConnected(e));

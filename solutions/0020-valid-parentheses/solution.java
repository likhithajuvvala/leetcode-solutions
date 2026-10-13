class Solution {
    public boolean isValid(String s) {
        Deque<Character>stack = new ArrayDeque<>();
        for(char c: s.toCharArray()){
            if(c=='('||c=='['||c=='{'){
                stack.push(c);
            }
            else{
                if(stack.isEmpty()) return false;
                char open = stack.pop();
                if(c==')'&& open!='(') return false;
                if(c==']'&& open!='[') return false;
                if(c=='}'&& open!='{') return false;

            }
        }
        return stack.isEmpty();
    }
}
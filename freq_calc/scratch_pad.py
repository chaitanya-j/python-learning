import re

line = "Hello!! How 'are' @you & how is $#(){} your dad?? I ""am"" ^ *fine"

puncs = "[ " " ! "  "' ( $ ? % &) * +  - . / : ; < = > ? @  \ ^ _ ` { , # | } ~ " " ]"
mod_line = re.sub(puncs," ",line)
print(mod_line)
import sys
class Brainfuck:
    def __init__(self):
        self.code = []
        self.labels = []
        self.end= []
        self.loops = []
        self.mem = [0] * 600000
        self.actions = {
            '>': (None, self._incr_pos),
            '<': (None, lambda: self._incr_pos(-1)),
            '+': (None, self._incr_val),
            '-': (None, lambda: self._incr_val(-1)),
            '.': (None, self._put_char),
            ',': (None, self._get_char),
            '[': (self._enter_loop, self._cond_jmp),
            ']': (self._exit_loop, self._jmp)
        }

    def parse_string(self, s):
        for c in s:
            action = self.actions.get(c)
            if action:
                (action[0] or (lambda: self._append_instr(c)))()

    def _get_label(self):
        self.labels.append(None)
        return len(self.labels) - 1

    def _put_label(self, label):
        self.labels[label] = len(self.code)

    def _append_instr(self, *instr):
        self.code.append(instr)

    def _enter_loop(self):
        label1, label2 = self._get_label(), self._get_label()
        self._put_label(label1)
        self._append_instr('[', label2)
        self.loops.append((label1, label2))

    def _exit_loop(self):
        label1, label2 = self.loops.pop()
        self._append_instr(']', label1)
        self._put_label(label2)

    def _incr_pos(self, i=1):
        self.pos += i

    def _incr_val(self, i=1):
        self.mem[self.pos] += i

    def _put_char(self):
        self.end.append(chr(self.mem[self.pos]))

    def _get_char(self):
        self.mem[self.pos] = ord(sys.stdin.read(1))

    def _jmp(self, label):
        self.pc = self.labels[label] - 1

    def _cond_jmp(self, label):
        if not self.mem[self.pos]:
            self._jmp(label)

    def execute(self):
        assert len(self.loops) == 0
        self.pc = 0
        self.pos = 0
        while self.pc < len(self.code):
            instr, *args = self.code[self.pc]
            _, action = self.actions.get(instr)
            action(*args)
            self.pc += 1
        a = (''.join([i for i in self.end]))
        return a


def rot3(s):
    final = []
    for char in s:
        final.append(char)
    for num in range(len(final)):
        final[num] = ord(final[num]) - 3
    for renum in range(len(final)):
        final[renum] = chr(final[renum])
    bf = Brainfuck()
    bf.parse_string(''.join([i for i in final]))
    return bf.execute()

def start(made):
    final = []
    s = []
    t=made
    t=t.split('0x')
    for i in t:
        try:
            final.append(int(i,16))
        except: continue
    for i in final:
        s.append(chr(i))
    return rot3(''.join([i for i in s]))

def b16(a):
    x=[]
    for i in a:
        x.append(hex(ord(i)))
    return ''.join([i for i in x])

def rot32(s):
    final = []
    for char in s:
        final.append(char)
    for num in range(len(final)):
        final[num] = ord(final[num]) + 3
    for renum in range(len(final)):
        final[renum] = chr(final[renum])
    return b16(''.join([i for i in final]))

def letter_to_brainfuck(letter):
    num = ord(letter)
    return '+'*int(num / 10) + '[>++++++++++<-]>' + '+'*(num % 10)

def brainfuck_print(letter_list):
    return rot32(''.join([i +'.>' for i in letter_list]))
Gamma={'0','1','b'}
Sigma={'0','1'}
Transition = dict(q1=dict(),q2=dict(),q3=dict(),q4=dict())

# Testing
if __name__ == "__main__":
    text = 'b'
    if text in Gamma:
        print("yes")
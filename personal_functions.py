
def euclidean_distance(np1, np2):
    np_diff_squared = (np1 - np2)**2
    np_hyp_squared = np_diff_squared.sum(axis = 1)
    return np.sqrt(np_hyp_squared).reshape(len(np_hyp_squared),1)

def main():
    pass

if __name__ == '__main__':
    main()
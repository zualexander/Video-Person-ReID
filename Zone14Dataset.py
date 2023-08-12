import os.path as osp
import pickle


class Zone14DataSet(object):
    dataset_dir = 'data'

    def __init__(self, root='generated_data', **kwargs):
        self.root = osp.abspath(osp.expanduser(root))
        self.dataset_dir = osp.join(self.root, self.dataset_dir)

        # All you need to do here is to generate three lists,
        # which are train, query and gallery.
        # Each list contains tuples of (img_path, pid, camid),
        # where
        # - img_path (str): absolute path to an image.
        # - pid (int): person ID, e.g. 0, 1.
        # - camid (int): camera ID, e.g. 0, 1.
        # Note that
        # - pid and camid should be 0-based.
        # - query and gallery should share the same pid scope (e.g.
        #   pid=0 in query refers to the same person as pid=0 in gallery).
        # - train, query and gallery share the same camid scope (e.g.
        #   camid=0 in train refers to the same camera as camid=0
        #   in query/gallery).
        with open(f'{self.root}/info/train', 'rb') as fp:
            self.train = pickle.load(fp)
        with open(f'{self.root}/info/gallery', 'rb') as fp:
            self.gallery = pickle.load(fp)
        with open(f'{self.root}/info/query', 'rb') as fp:
            self.query = pickle.load(fp)

        self.num_train_pids =

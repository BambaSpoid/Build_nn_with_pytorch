import matplotlib.pyplot as plt
import torchvision.transforms as transforms


transform = transforms.Compose([transforms.RandomResizedCrop(224),
                                       transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(),
                                       transforms.Normalize([0.485, 0.456, 0.406],
                                                            [0.229, 0.224, 0.225])])

def plot(train_loss, val_loss):

    plt.title("Training results: Loss")
    plt.plot(val_loss,label='val_loss')
    plt.plot(train_loss, label="train_loss")
    plt.savefig()
    plt.legend()
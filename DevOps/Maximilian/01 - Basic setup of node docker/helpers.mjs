const connectToDatabase = () => {
  const dummyPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log("Resolving promise...")
        resolve();
    }, 1000);
  });

  return dummyPromise;
};

export default connectToDatabase;
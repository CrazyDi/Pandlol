const timer = {};

timer.start = (callback, interval, step) => {
    let percent = 0;

    const timer = () => {
        window.setTimeout(() => {
            percent += (step || 1);

            if (percent > 100) {
                percent = 100;
            }

            callback(percent);

            if (percent < 100) {
                timer();
            }
        }, interval);
    };

    timer();
};

export default timer;

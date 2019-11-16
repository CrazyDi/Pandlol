const api = {};

const temp = [
    {},
    {},
    {},
    {}
];

api.search = function(filter) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve({
                data: temp
            });
        }, 2000);
    });
};

export default api;

from sklearn.preprocessing import StandardScaler

from sklearn.cluster import MiniBatchKMeans


def train_model(

    customer,

    k=4

):

    X = customer[

        [

            'Age',

            'AvgBalance',

            'TotalTransaction',

            'AvgTransaction',

            'TransactionCount'

        ]

    ]


    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)


    model = MiniBatchKMeans(

        n_clusters=k,

        batch_size=2048,

        random_state=42,

        n_init=3

    )


    customer['Cluster'] = (

        model.fit_predict(

            X_scaled

        )

    )


    return customer, model, scaler
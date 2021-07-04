import React from 'react'
import Label from 'controls/Label'
import IChampionList from 'app/interfaces/IChampionList'
import HomePageSearchResultItem from './Item'
import useStyles from './styles'

interface Props {
    championList: IChampionList
}

const HomePageSearchResult = (props: Props) => {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <div>
                <Label>Search Results:</Label>
                {props.championList.items.length === 0 &&
                    <Label>No items found</Label>
                }
                {props.championList.items.length > 0 &&
                    <Label>Found items: {props.championList.items.length}, total: {props.championList.total}</Label>
                }
                {props.championList.items.length > 0 &&
                    props.championList.items.map((item) =>
                        <HomePageSearchResultItem item={item}/>
                    )
                }
            </div>
        </div>
    )
}

export default HomePageSearchResult

import React, { useState } from 'react'
import Label from 'controls/Label'
import MasterPage from 'app/components/MasterPage'
import useApi from 'app/hooks/useApi'
import IError from 'app/interfaces/IError'
import IChampionList from 'app/interfaces/IChampionList'
import IChampionListFilter from 'app/interfaces/IChampionListFilter'
import HomePageSearchFilter from './SearchFilter'
import HomePageSearchResult from './SearchResult'
import useStyles from './styles'

interface Props {
}

const HomePage = (props: Props) => {
    const classes = useStyles()
    const api = useApi()
    const [championList, setChampionList] = useState<IChampionList | null>(null)

    const handleSearch = (filter: IChampionListFilter) => {
        api.getChampions(filter)
            .then((championList: IChampionList) => {
                setChampionList(championList)
            })
            .catch((error: IError) => {
            })
    }

    return (
        <MasterPage>
            <div className={classes.root}>
                <Label>Home Page</Label>
                <br/>

                <HomePageSearchFilter onSearch={handleSearch} />

                {!championList &&
                    <Label>No Search</Label>
                }
                {championList &&
                    <HomePageSearchResult championList={championList} />
                }
            </div>
        </MasterPage>
    )
}

export default HomePage

#!/bin/bash

#model=FLOR
#expname=CTL1860_tiger3_intelmpi_24_1116PE
#model=AM2.5C360
#expname=CTL1990s_tiger3_intelmpi_24_2430PE
model=CM2.1
expname=CTL1860_tiger3_intelmpi_24_60PE
#year_extend=202411
#root_modelout=/tigress/wenchang/MODEL_OUT/${model}/tiger3/amipHadISSTlongChancorr_tiger3_intelmpi_24_1440PE_extend${year_extend}
#if [ ! -e archive_extend${year_extend} ]; then
#    ln -s $root_modelout archive_extend${year_extend}
#    echo "[link created]: archive_extend${year_extend} -> $root_modelout"
#fi
#for ii in 6 7 8 9 10; 
#for ii in {1..5}; do
    #dir_src=/home/wenchang/${model}/work/amipHadISSTlongChancorr_tiger3_intelmpi_24_1440PE_extend${year_extend}_e${ii}
    #if [ $ii -lt 10 ]; then
    #    dir_dst=$root_modelout/en0$ii
    #else
    #    dir_dst=$root_modelout/en$ii
    #fi
    dir_src=/home/wenchang/${model}/work/${expname}
    #dir_dst=/projects/GEOCLIM/wenchang/MODEL_OUT2/${model}/${expname}
    dir_dst=/projects/GEOCLIM/wenchang/MODEL_OUT/${model}/tiger3/${expname}
    
    if [ ! -d "$dir_dst" ]; then
        mkdir -p $dir_dst
        echo "Dir Created: $dir_dst"
        ln -s $dir_dst archive
        echo "[link created]: archive -> $dir_dst"
    fi
    
    echo From: $dir_src
    echo To:   $dir_dst
    echo Start ...
    echo 
    
    #rsync -avhP $dir_src/TC/analysis_lmh $dir_dst/
    rsync -avhP $dir_src/RESTART $dir_dst/
    rsync -avhP $dir_src/POSTP $dir_dst/
    
    if [ "$?" -eq 0 ]; then
        echo
        echo From: $dir_src
        echo To:   $dir_dst
        echo Done.
        echo
    fi
#done
